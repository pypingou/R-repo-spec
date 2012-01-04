%global packname  GeneR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.24.0
Release:          1%{?dist}
Summary:          R for genes and sequences analysis

Group:            Applications/Engineering 
License:          CeCILL-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package manipulating nucleotidic sequences (Embl, Fasta, GenBank)

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
%doc %{rlibdir}/GeneR/html
%doc %{rlibdir}/GeneR/DESCRIPTION
%doc %{rlibdir}/GeneR/doc
%{rlibdir}/GeneR/help
%{rlibdir}/GeneR/R
%{rlibdir}/GeneR/INDEX
%{rlibdir}/GeneR/NAMESPACE
%{rlibdir}/GeneR/libs
%{rlibdir}/GeneR/demo
%{rlibdir}/GeneR/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.24.0-1
- initial package for Fedora