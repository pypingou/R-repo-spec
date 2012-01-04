%global packname  EVER
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Estimation of Variance by Efficient Replication

Group:            Applications/Engineering 
License:          file LICENCE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Delete-A-Group Jackknife replication. Calibration of replicate weights.
Estimates, standard errors and confidence intervals for: totals, means,
absolute and relative frequency distributions, contingency tables, ratios,
quantiles and regression coefficients. Estimates, standard errors and
confidence intervals for user-defined estimators (even non-analytic).
Domain (subpopulation) estimation.

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
%doc %{rlibdir}/EVER/DESCRIPTION
%doc %{rlibdir}/EVER/NEWS
%doc %{rlibdir}/EVER/LICENCE
%doc %{rlibdir}/EVER/html
%doc %{rlibdir}/EVER/CITATION
%{rlibdir}/EVER/DISCLAIMER
%{rlibdir}/EVER/help
%{rlibdir}/EVER/README
%{rlibdir}/EVER/Meta
%{rlibdir}/EVER/data
%{rlibdir}/EVER/R
%{rlibdir}/EVER/NAMESPACE
%{rlibdir}/EVER/INDEX
%{rlibdir}/EVER/user.estimators

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora