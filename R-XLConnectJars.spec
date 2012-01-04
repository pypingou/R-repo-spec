%global packname  XLConnectJars
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          JAR dependencies for the XLConnect package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
This package provides external JAR dependencies for the XLConnect package

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/XLConnectJars/DESCRIPTION
%doc %{rlibdir}/XLConnectJars/NEWS
%doc %{rlibdir}/XLConnectJars/html
%{rlibdir}/XLConnectJars/NAMESPACE
%{rlibdir}/XLConnectJars/help
%{rlibdir}/XLConnectJars/Meta
%{rlibdir}/XLConnectJars/INDEX
%{rlibdir}/XLConnectJars/java
%{rlibdir}/XLConnectJars/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora