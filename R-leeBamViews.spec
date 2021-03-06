%global packname  leeBamViews
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.13
Release:          1%{?dist}
Summary:          leeBamViews -- multiple yeast RNAseq samples excerpted from Lee 2009

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-Rsamtools R-BSgenome 

BuildRequires:    R-devel tex(latex) R-Biobase R-Rsamtools R-BSgenome 

%description
data from PMID 19096707; prototype for managing multiple NGS samples

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.13-1
- initial package for Fedora