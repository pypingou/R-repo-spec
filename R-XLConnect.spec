%global packname  XLConnect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Excel Connector for R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-XLConnectJars R-XLConnectJars R-rJava R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-XLConnectJars R-XLConnectJars R-rJava R-utils R-methods 

%description
Manipulate Excel files from R

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora