%global packname  RNAinteract
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Estimate Pairwise Interactions from multidimensional features

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-abind R-locfit R-Biobase 

BuildRequires:    R-devel tex(latex) R-abind R-locfit R-Biobase 

%description
RNAinteract estimates genetic interactions from multi-dimensional
read-outs like features extracted from images. The screen is assumed to be
performed in multi-well plates or similar designs. Starting from a list of
features (e.g. cell number, area, fluorescence intensity) per well,
genetic interactions are estimated. The packages provides functions for
reporting interacting gene pairs, plotting heatmaps and double RNAi plots.
An HTML report can be written for quality control and analysis.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora