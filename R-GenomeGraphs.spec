%global packname  GenomeGraphs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          Plotting genomic information from Ensembl

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-biomaRt R-grid 


BuildRequires:    R-devel tex(latex) R-methods R-biomaRt R-grid



%description
Genomic data analyses requires integrated visualization of known genomic
information and new experimental data.  GenomeGraphs uses the biomaRt
package to perform live annotation queries to Ensembl and translates this
to e.g. gene/transcript structures in viewports of the grid graphics
package. This results in genomic information plotted together with your
data.  Another strength of GenomeGraphs is to plot different data types
such as array CGH, gene expression, sequencing and other data, together in
one plot using the same genome coordinate system.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora