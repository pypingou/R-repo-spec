%global packname  cellHTS2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.18.0
Release:          1%{?dist}
Summary:          Analysis of cell-based screens - revised version of cellHTS

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RColorBrewer R-Biobase R-methods R-genefilter R-splots R-vsn R-hwriter R-locfit R-grid 

BuildRequires:    R-devel tex(latex) R-RColorBrewer R-Biobase R-methods R-genefilter R-splots R-vsn R-hwriter R-locfit R-grid 

%description
Analysis of cell-based RNA interference screens. See ?cellHTS2 for a brief

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.18.0-1
- initial package for Fedora