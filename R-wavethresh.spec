%global packname  wavethresh
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.5
Release:          1%{?dist}
Summary:          Wavelets statistics and transforms.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Performs 1, 2 and 3D wavelet transforms, nondecimated transforms, wavelet
packet transforms, nondecimated wavelet packet transforms, multiple
wavelet transforms, complex-valued wavelet transforms, wavelet shrinkage
for various kinds of data, locally stationary wavelet time series,
nonstationary multiscale transfer function modeling, density estimation.

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
%doc %{rlibdir}/wavethresh/DESCRIPTION
%doc %{rlibdir}/wavethresh/html
%{rlibdir}/wavethresh/Meta
%{rlibdir}/wavethresh/libs
RPM build errors:
%{rlibdir}/wavethresh/data
%{rlibdir}/wavethresh/R
%{rlibdir}/wavethresh/NAMESPACE
%{rlibdir}/wavethresh/help
%{rlibdir}/wavethresh/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.5-1
- initial package for Fedora