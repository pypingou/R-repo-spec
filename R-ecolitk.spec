%global packname  ecolitk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Meta-data and tools for E. coli

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-graphics R-methods 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-graphics R-methods 


%description
Meta-data and tools to work with E. coli. The tools are mostly plotting
functions to work with circular genomes. They can used with other

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
%doc %{rlibdir}/ecolitk/DESCRIPTION
%doc %{rlibdir}/ecolitk/doc
%doc %{rlibdir}/ecolitk/html
%{rlibdir}/ecolitk/data
%{rlibdir}/ecolitk/Meta
%{rlibdir}/ecolitk/R
%{rlibdir}/ecolitk/NAMESPACE
%{rlibdir}/ecolitk/INDEX
%{rlibdir}/ecolitk/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora