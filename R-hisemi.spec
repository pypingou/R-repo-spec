%global packname  hisemi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.191
Release:          1%{?dist}
Summary:          Hierarchical Semiparametric Regression of Test Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-191.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-Matrix R-Iso R-splines R-fda 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Matrix R-Iso R-splines R-fda 


%description
This package implements methods for hierarchical semiparametric regression
models for test statistics. Specifically, test statistics given the
null/alternative hypotheses are modeled parametrically, whereas the
unobservable status of null/alternative hypotheses are modeled using
nonparametric addtive logistic regression over covariates.

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
%doc %{rlibdir}/hisemi/DESCRIPTION
%doc %{rlibdir}/hisemi/html
%{rlibdir}/hisemi/help
%{rlibdir}/hisemi/R
%{rlibdir}/hisemi/INDEX
%{rlibdir}/hisemi/NAMESPACE
RPM build errors:
%{rlibdir}/hisemi/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.191-1
- initial package for Fedora