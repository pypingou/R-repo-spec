%global packname  GExMap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          A visual, intuitive, easy to use software giving access to a new type of information buried into your microarray data.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-multtest 

BuildRequires:    R-devel tex(latex) R-Biobase R-multtest 

%description
Perform statistical tests to unveil genomic clusters, produces garphical
interpretations of the statistical results in pdf files, perform a Gene
Ontology analysis and produces graphic results in pdf files

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
%doc %{rlibdir}/GExMap/DESCRIPTION
%doc %{rlibdir}/GExMap/html
%{rlibdir}/GExMap/NAMESPACE
%{rlibdir}/GExMap/Meta
%{rlibdir}/GExMap/R
%{rlibdir}/GExMap/INDEX
%{rlibdir}/GExMap/help
%{rlibdir}/GExMap/data

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora