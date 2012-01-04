%global packname  PSCBS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.17.1
Release:          1%{?dist}
Summary:          Analysis of Parent-Specific DNA Copy Numbers

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 R-R.utils 
Requires:         R-DNAcopy 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.utils
BuildRequires:    R-DNAcopy 


%description
Segments allele-specific DNA copy number data to detect regions with
abnormal copy number within each parental chromosome

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
%doc %{rlibdir}/PSCBS/NEWS
%doc %{rlibdir}/PSCBS/html
%doc %{rlibdir}/PSCBS/DESCRIPTION
%{rlibdir}/PSCBS/INDEX
%{rlibdir}/PSCBS/Meta
%{rlibdir}/PSCBS/NAMESPACE
%{rlibdir}/PSCBS/R
%{rlibdir}/PSCBS/data-ex
%{rlibdir}/PSCBS/help

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.17.1-1
- initial package for Fedora