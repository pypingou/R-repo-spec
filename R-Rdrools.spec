%global packname  Rdrools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          A rules engine for R based on Drools

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-Rdroolsjars 
Requires:         R-rJava R-Rdroolsjars 

BuildRequires:    R-devel tex(latex) R-rJava R-Rdroolsjars
BuildRequires:    R-rJava R-Rdroolsjars 


%description
Rdrools is a rules engine for R based on the popular Java Drools engine

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
%doc %{rlibdir}/Rdrools/DESCRIPTION
%doc %{rlibdir}/Rdrools/html
%{rlibdir}/Rdrools/INDEX
%{rlibdir}/Rdrools/java
%{rlibdir}/Rdrools/NAMESPACE
%{rlibdir}/Rdrools/help
%{rlibdir}/Rdrools/Meta
%{rlibdir}/Rdrools/LICENSE
%{rlibdir}/Rdrools/R
%{rlibdir}/Rdrools/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora