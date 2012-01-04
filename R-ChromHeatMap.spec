%global packname  ChromHeatMap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Heat map plotting by genome coordinate

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-annotate R-AnnotationDbi R-hgu95av2.db 

BuildRequires:    R-devel tex(latex) R-annotate R-AnnotationDbi R-hgu95av2.db 

%description
The ChromHeatMap package can be used to plot genome-wide data (e.g.
expression, CGH, SNP) along each strand of a given chromosome as a heat
map. The generated heat map can be used to interactively identify probes
and genes of interest.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora