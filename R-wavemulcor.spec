%global packname  wavemulcor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Wavelet routine for multiple correlation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-waveslim 


BuildRequires:    R-devel tex(latex) R-waveslim



%description
Wavelet routines that calculate single sets of wavelet multiple
correlations and cross-correlations out of n variables (either 1D time
series, 2D images or 3D arrays). They can later be plotted in single
graphs, as an alternative to trying to make sense out of several sets of
wavelet correlations or wavelet cross-correlations. The code is based on
the calculation, at each wavelet scale, of the square root of the
coefficient of determination in a linear combination of variables for
which such coefficient of determination is a maximum. The code provided
here is based on the wave.correlation routine in Brandon Whitcher's
waveslim R package Version: 1.6.4, which in turn is based on wavelet
methodology developed in Percival and Walden (2000); Gencay, Selcuk and
Whitcher (2001) and others.

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
%doc %{rlibdir}/wavemulcor/DESCRIPTION
%doc %{rlibdir}/wavemulcor/html
%{rlibdir}/wavemulcor/NAMESPACE
RPM build errors:
%{rlibdir}/wavemulcor/help
%{rlibdir}/wavemulcor/Meta
%{rlibdir}/wavemulcor/INDEX
%{rlibdir}/wavemulcor/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora