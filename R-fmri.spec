%global packname  fmri
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          Analysis of fMRI experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
The package contains R-functions to perform an fmri analysis as described
in K. Tabelow, J. Polzehl, H.U. Voss, and V. Spokoiny, Analysing fMRI
experiments with structure adaptive smoothing procedures, NeuroImage,
33:55-62 (2006) and J. Polzehl, H.U. Voss, K. Tabelow, Structural adaptive
segmentation for statistical parametric mapping, NeuroImage, 52:515-523

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
%doc %{rlibdir}/fmri/html
%doc %{rlibdir}/fmri/DESCRIPTION
%doc %{rlibdir}/fmri/CITATION
%{rlibdir}/fmri/INDEX
%{rlibdir}/fmri/R
%{rlibdir}/fmri/NAMESPACE
%{rlibdir}/fmri/img
%{rlibdir}/fmri/libs
%{rlibdir}/fmri/Meta
%{rlibdir}/fmri/demo
%{rlibdir}/fmri/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora