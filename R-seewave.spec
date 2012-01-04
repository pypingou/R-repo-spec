%global packname  seewave
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Time wave analysis and graphical representation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-fftw R-rgl R-rpanel R-tcltk R-tuneR 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-fftw R-rgl R-rpanel R-tcltk R-tuneR 


%description
seewave provides functions for analysing, manipulating, displaying,
editing and synthesizing time waves (particularly sound).  This package
processes time analysis (oscillograms and envelopes), spectral content,
resonance quality factor, entropy, cross correlation and autocorrelation,
zero-crossing, dominant frequency, analytic signal, frequency coherence,
2D and 3D spectrograms and many other analyses.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.1-1
- initial package for Fedora