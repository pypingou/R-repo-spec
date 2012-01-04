%global packname  arm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.14
Release:          1%{?dist}
Summary:          Data Analysis Using Regression and Multilevel/Hierarchical Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-MASS R-Matrix R-lme4 R-R2WinBUGS R-abind 
Requires:         R-Matrix R-lme4 R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-MASS R-Matrix R-lme4 R-R2WinBUGS R-abind
BuildRequires:    R-Matrix R-lme4 R-stats 


%description
R functions for processing lm, glm, mer and polr outputs.

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
%doc %{rlibdir}/arm/DESCRIPTION
%doc %{rlibdir}/arm/html
%{rlibdir}/arm/data
%{rlibdir}/arm/help
%{rlibdir}/arm/INDEX
%{rlibdir}/arm/Meta
RPM build errors:
%{rlibdir}/arm/R
%{rlibdir}/arm/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.14-1
- initial package for Fedora