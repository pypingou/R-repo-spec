%global packname  sbgcop
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.975
Release:          1%{?dist}
Summary:          Semiparametric Bayesian Gaussian copula estimation and imputation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package estimates parameters of a Gaussian copula, treating the
univariate marginal distributions as nuisance parameters as described in
Hoff(2007). It also provides a semiparametric imputation procedure for
missing multivariate data.

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
%doc %{rlibdir}/sbgcop/html
%doc %{rlibdir}/sbgcop/DESCRIPTION
%{rlibdir}/sbgcop/R
%{rlibdir}/sbgcop/Meta
%{rlibdir}/sbgcop/help
%{rlibdir}/sbgcop/INDEX
%{rlibdir}/sbgcop/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.975-1
- initial package for Fedora