%global packname  vegetarian
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Jost Diversity Measures for Community Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
This package computes diversity for community data sets using the methods
outlined by Jost (2006, 2007). While there are differing opinions on the
ideal way to calculate diversity (e.g. Magurran 2004), this method offers
the advantage of providing diversity numbers equivalents, independent
alpha and beta diversities, and the ability to incorporate 'order' (q) as
a continuous measure of the importance of rare species in the metrics. The
functions provided in this package largely correspond with the equations
offered by Jost in the cited papers. The package computes alpha
diversities, beta diversities, gamma diversities, and similarity indices.
Confidence intervals for diversity measures are calculated using a
bootstrap method described by Chao et al. (2008).  For datasets with many
samples (sites, plots), sim.table creates tables of all pairwise
comparisons possible, and for grouped samples sim.groups calculates
pairwise combinations of within- and between-group comparisons.

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
%doc %{rlibdir}/vegetarian/DESCRIPTION
%doc %{rlibdir}/vegetarian/html
%{rlibdir}/vegetarian/NAMESPACE
%{rlibdir}/vegetarian/R
%{rlibdir}/vegetarian/Meta
%{rlibdir}/vegetarian/data
%{rlibdir}/vegetarian/help
%{rlibdir}/vegetarian/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora