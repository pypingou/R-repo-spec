%global packname  TilePlot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Characterization of functional genes in complex microbial communities using tiling DNA microarrays

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is intended for processing the output from functional gene
tiling DNA microarray experiments. It produces hybridization pattern plots
for each gene on the array, and statistics for each gene including mean
probe intensity, median probe intensity, bright probe fraction, bright
segment length dependent score, bright probe mean intensity, and bright
probe median intensity. Output is generated in order of bright segment
length dependent score in both a latex/eps format and tab-delimited text
file. The package works in two modes: single array, and comparison of two
arrays. Array comparison includes array comparison statistics: median of
logarithm of one array probe divided by its counterpart on the other
array, median absolute deviation of that value, and the binomial test to
see whether the genes are equally abundant in both arrays.

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
%doc %{rlibdir}/TilePlot/html
%doc %{rlibdir}/TilePlot/DESCRIPTION
%{rlibdir}/TilePlot/Meta
%{rlibdir}/TilePlot/allgenesonchip.ID
%{rlibdir}/TilePlot/array2
%{rlibdir}/TilePlot/array1
%{rlibdir}/TilePlot/R
%{rlibdir}/TilePlot/help
%{rlibdir}/TilePlot/INDEX
%{rlibdir}/TilePlot/NAMESPACE
%{rlibdir}/TilePlot/all_annotations

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora