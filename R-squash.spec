%global packname  squash
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Color-based plots for multivariate visualization

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grDevices 

BuildRequires:    R-devel tex(latex) R-grDevices 

%description
This package provides functions for color-based visualization of
multivariate data, i.e. colorgrams or heatmaps.  Lower-level functions are
provided to map numeric values to colors, display a matrix as an array of
colors, and draw color keys.  Higher-level plotting functions are provided
to generate a bivariate histogram, a dendrogram aligned with a color-coded
matrix, a triangular distance matrix, and more.

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
%doc %{rlibdir}/squash/html
%doc %{rlibdir}/squash/NEWS
%doc %{rlibdir}/squash/DESCRIPTION
%{rlibdir}/squash/NAMESPACE
%{rlibdir}/squash/help
%{rlibdir}/squash/R
%{rlibdir}/squash/INDEX
%{rlibdir}/squash/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora