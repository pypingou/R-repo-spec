%global packname  huge
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          High-dimensional Undirected Graph Estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-lattice R-igraph R-MASS 

BuildRequires:    R-devel tex(latex) R-Matrix R-lattice R-igraph R-MASS 

%description
The package "huge" provides a general framework for high-dimensional
undirected graph estimation. It integrates data preprocessing,
neighborhood screening, graph estimation, and model selection techniques
into a pipeline. In preprocessing stage, the nonparanormal(npn)
transformation is applied to help relax the normality assumption. In the
graph estimation stage, the graph structure is estimated by
Meinshausen-Buhlmann graph estimation or the graphical lasso, and both
methods can be further accelerated by the lossy screening rule
preselecting the neighborhood of each variable by correlation
thresholding. We target on high-dimensional data analysis usually d >> n,
and the computation is memory-optimized using the sparse matrix output. We
also provide a computationally efficient approach, correlation
thresholding graph estimation. Three regularization/thresholding parameter
selection methods are included in this package: (1)stability approach for
regularization selection (2) rotation information criterion (3) extended
Bayesian information criterion which is only available for the graphical

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora