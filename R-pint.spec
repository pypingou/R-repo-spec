%global packname  pint
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Pairwise INTegration of functional genomics data

Group:            Applications/Engineering 
License:          FreeBSD
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-methods R-graphics R-Matrix R-dmt 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-methods R-graphics R-Matrix R-dmt 

%description
Pairwise data integration for functional genomics. In particular, tools to
screen functionally active chromosomal aberrations from paired copy
number, gene expression and miRNA measurements from the same patients.

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
%doc %{rlibdir}/pint/NEWS
%doc %{rlibdir}/pint/CITATION
%doc %{rlibdir}/pint/html
%doc %{rlibdir}/pint/doc
%doc %{rlibdir}/pint/DESCRIPTION
%{rlibdir}/pint/LICENSE
%{rlibdir}/pint/Meta
%{rlibdir}/pint/NAMESPACE
%{rlibdir}/pint/R
%{rlibdir}/pint/data
%{rlibdir}/pint/help
%{rlibdir}/pint/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora