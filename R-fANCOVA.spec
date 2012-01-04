%global packname  fANCOVA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Nonparametric Analysis of Covariance

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains a collection of R functions to perform nonparametric
analysis of covariance for regression curves or surfaces. Testing the
equality or parallelism of nonparametric curves or surfaces is equivalent
to analysis of variance (ANOVA) or analysis of covariance (ANCOVA) for
one-sample functional data. Three different testing methods are available
in the package, including one based on L-2 distance, one based on an ANOVA
statistic, and one based on variance estimators.

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
%doc %{rlibdir}/fANCOVA/NEWS
%doc %{rlibdir}/fANCOVA/html
%doc %{rlibdir}/fANCOVA/DESCRIPTION
%{rlibdir}/fANCOVA/INDEX
%{rlibdir}/fANCOVA/LICENSE
%{rlibdir}/fANCOVA/help
%{rlibdir}/fANCOVA/Meta
%{rlibdir}/fANCOVA/data
%{rlibdir}/fANCOVA/R
%{rlibdir}/fANCOVA/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora