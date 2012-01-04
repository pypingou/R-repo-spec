%global packname  RWekajars
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.7.5.1
Release:          1%{?dist}
Summary:          R/Weka interface jars

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.7.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-rJava 


%description
External jars required for package RWeka.

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
%doc %{rlibdir}/RWekajars/DESCRIPTION
%doc %{rlibdir}/RWekajars/html
%{rlibdir}/RWekajars/Meta
%{rlibdir}/RWekajars/java
%{rlibdir}/RWekajars/help
%{rlibdir}/RWekajars/R
%{rlibdir}/RWekajars/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.7.5.1-1
- initial package for Fedora