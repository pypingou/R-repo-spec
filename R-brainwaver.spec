%global packname  brainwaver
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Basic wavelet analysis of multivariate time series with a visualisation and parametrisation using graph theory.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-waveslim 

BuildRequires:    R-devel tex(latex) R-waveslim 

%description
This package computes the correlation matrix for each scale of a wavelet
decomposition, namely the one performed by the R package waveslim
(Whitcher, 2000). An hypothesis test is applied to each entry of one
matrix in order to construct an adjacency matrix of a graph. The graph
obtained is finally analysed using the small-world theory (Watts and
Strogatz, 1998) and using the computation of efficiency (Latora, 2001),
tested using simulated attacks. The brainwaver project is complementary to
the camba project for brain-data preprocessing. A collection of scripts
(with a makefile) is avalaible to download along with the brainwaver
package, see information on the webpage mentioned below.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora