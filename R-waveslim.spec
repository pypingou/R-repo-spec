%global packname  waveslim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.4
Release:          1%{?dist}
Summary:          Basic wavelet routines for one-, two- and three-dimensional signal processing

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-grDevices 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-grDevices 

%description
Basic wavelet routines for time series (1D), image (2D) and array (3D)
analysis.  The code provided here is based on wavelet methodology
developed in Percival and Walden (2000); Gencay, Selcuk and Whitcher
(2001); the dual-tree complex wavelet transform (CWT) from Kingsbury
(1999, 2001) as implemented by Selesnick; and Hilbert wavelet pairs
(Selesnick 2001, 2002).  All figures in chapters 4-7 of GSW (2001) are
reproducible using this package and R code available at the book
website(s) below.

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
%doc %{rlibdir}/waveslim/html
%doc %{rlibdir}/waveslim/DESCRIPTION
%{rlibdir}/waveslim/Meta
%{rlibdir}/waveslim/help
%{rlibdir}/waveslim/libs
%{rlibdir}/waveslim/INDEX
%{rlibdir}/waveslim/R
RPM build errors:
%{rlibdir}/waveslim/NAMESPACE
%{rlibdir}/waveslim/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.4-1
- initial package for Fedora