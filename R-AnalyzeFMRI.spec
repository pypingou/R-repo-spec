%global packname  AnalyzeFMRI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.14
Release:          1%{?dist}
Summary:          Functions for analysis of fMRI datasets stored in the ANALYZE or NIFTI format.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-R.matlab R-fastICA 

BuildRequires:    R-devel tex(latex) R-tcltk R-R.matlab R-fastICA 

%description
Functions for I/O, visualisation and analysis of functional Magnetic
Resonance Imaging (fMRI) datasets stored in the ANALYZE or NIFTI format.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.14-1
- initial package for Fedora