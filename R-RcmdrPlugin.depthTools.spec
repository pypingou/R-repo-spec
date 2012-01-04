%global packname  RcmdrPlugin.depthTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          R commander Depth Tools Plug-In

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-depthTools 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-depthTools 

%description
This package provides an Rcmdr plug-in based on the depthTools package,
which implements different robust statistical tools for the description
and analysis of gene expression data based on the Modified Band Depth,
namely, the scale curves for visualizing the dispersion of one or various
groups of samples (e.g. types of tumors), a rank test to decide whether
two groups of samples come from a single distribution and two methods of
supervised classification techniques, the DS and TAD methods.

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
%doc %{rlibdir}/RcmdrPlugin.depthTools/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.depthTools/html
%{rlibdir}/RcmdrPlugin.depthTools/INDEX
%{rlibdir}/RcmdrPlugin.depthTools/R
%{rlibdir}/RcmdrPlugin.depthTools/etc
%{rlibdir}/RcmdrPlugin.depthTools/Meta
%{rlibdir}/RcmdrPlugin.depthTools/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora