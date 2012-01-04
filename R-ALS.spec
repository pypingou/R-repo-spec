%global packname  ALS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          multivariate curve resolution alternating least squares (MCR-ALS)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nnls R-Iso 

BuildRequires:    R-devel tex(latex) R-nnls R-Iso 

%description
Alternating least squares is often used to resolve components contributing
to data with a bilinear structure; the basic technique may be extended to
alternating constrained least squares.  Commonly applied constraints
include unimodality, non-negativity, and normalization of components.
Several data matrices may be decomposed simultaneously by assuming that
one of the two matrices in the bilinear decomposition is shared between

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
%doc %{rlibdir}/ALS/NEWS
%doc %{rlibdir}/ALS/html
%doc %{rlibdir}/ALS/DESCRIPTION
%{rlibdir}/ALS/INDEX
%{rlibdir}/ALS/help
%{rlibdir}/ALS/Meta
%{rlibdir}/ALS/data
%{rlibdir}/ALS/R
%{rlibdir}/ALS/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora