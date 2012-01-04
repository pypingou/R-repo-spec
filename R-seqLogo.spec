%global packname  seqLogo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Sequence logos for DNA sequence alignments

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-grid 

BuildRequires:    R-devel tex(latex) R-methods R-grid 

%description
seqLogo takes the position weight matrix of a DNA sequence motif and plots
the corresponding sequence logo as introduced by Schneider and Stephens

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
%doc %{rlibdir}/seqLogo/html
%doc %{rlibdir}/seqLogo/DESCRIPTION
%doc %{rlibdir}/seqLogo/doc
%{rlibdir}/seqLogo/help
%{rlibdir}/seqLogo/Exfiles
%{rlibdir}/seqLogo/NAMESPACE
%{rlibdir}/seqLogo/Meta
%{rlibdir}/seqLogo/INDEX
%{rlibdir}/seqLogo/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora