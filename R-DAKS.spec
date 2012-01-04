%global packname  DAKS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Data Analysis and Knowledge Spaces

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-relations R-sets 


BuildRequires:    R-devel tex(latex) R-relations R-sets



%description
Functions and an example dataset for the psychometric theory of knowledge
spaces.  This package implements data analysis methods and procedures for
simulating data and quasi orders and transforming different formulations
in knowledge space theory.

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
%doc %{rlibdir}/DAKS/CITATION
%doc %{rlibdir}/DAKS/html
%doc %{rlibdir}/DAKS/doc
%doc %{rlibdir}/DAKS/DESCRIPTION
%{rlibdir}/DAKS/help
%{rlibdir}/DAKS/INDEX
%{rlibdir}/DAKS/Meta
%{rlibdir}/DAKS/NAMESPACE
%{rlibdir}/DAKS/R
%{rlibdir}/DAKS/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.1-1
- initial package for Fedora