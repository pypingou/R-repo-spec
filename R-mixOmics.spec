%global packname  mixOmics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Omics Data Integration Project

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-igraph R-rgl R-lattice 


BuildRequires:    R-devel tex(latex) R-igraph R-rgl R-lattice



%description
The package supplies two efficients methodologies: regularized CCA and
sparse PLS to unravel relationships between two heterogeneous data sets of
size (nxp) and (nxq) where the p and q variables are measured on the same
samples or individuals n. These data may come from high throughput
technologies, such as omics data (e.g. transcriptomics, metabolomics or
proteomics data) that require an integrative or joint analysis. However,
mixOmics can also be applied to any other large data sets where p + q >>
n. rCCA is a regularized version of CCA to deal with the large number of
variables. sPLS allows variable selection in a one step procedure and two
frameworks are proposed: regression and canonical analysis. Numerous
graphical outputs are provided to help interpreting the results.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0-1
- initial package for Fedora