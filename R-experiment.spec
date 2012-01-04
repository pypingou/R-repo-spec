%global packname  experiment
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          experiment: R package for designing and analyzing randomized experiments

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-MASS 

BuildRequires:    R-devel tex(latex) R-boot R-MASS 

%description
The package provides various statistical methods for designing and
analyzing randomized experiments. One main functionality of the package is
the implementation of randomized-block and matched-pair designs based on
possibly multivariate pre-treatment covariates. The package also provides
the tools to analyze various randomized experiments including cluster
randomized experiments, randomized experiments with noncompliance, and
randomized experiments with missing data.

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
%doc %{rlibdir}/experiment/DESCRIPTION
%doc %{rlibdir}/experiment/html
%{rlibdir}/experiment/libs
%{rlibdir}/experiment/R
%{rlibdir}/experiment/help
%{rlibdir}/experiment/INDEX
%{rlibdir}/experiment/Meta
%{rlibdir}/experiment/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora