%global packname  CompareTests
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimate diagnostic accuracy (sensitivity, specificity, etc) and agreement statistics when one test is conducted on only a subsample of specimens

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A standard test is observed on all specimens.  We treat the second test
(or sampled test) as being conducted on only a stratified sample of
specimens.  We treat the total sample as stratified two-phase sampling and
use inverse probability weighting.  We estimate diagnostic accuracy
(category-specific classification probabilities; for binary tests reduces
to specificity and sensitivity) and agreement statistics (percent
agreement, percent agreement by category, Kappa (unweighted), and symmetry
tests (reduces to McNemar's test for binary tests)).

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
%doc %{rlibdir}/CompareTests/DESCRIPTION
%doc %{rlibdir}/CompareTests/html
%{rlibdir}/CompareTests/NAMESPACE
%{rlibdir}/CompareTests/help
%{rlibdir}/CompareTests/Meta
%{rlibdir}/CompareTests/INDEX
%{rlibdir}/CompareTests/data
%{rlibdir}/CompareTests/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora