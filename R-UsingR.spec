%global packname  UsingR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.17
Release:          1%{?dist}
Summary:          Data sets for the text "Using R for Introductory Statistics"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
A collection of datasets to accompany the textbook "Using R for
Introductory Statistics."

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
%doc %{rlibdir}/UsingR/DESCRIPTION
%doc %{rlibdir}/UsingR/html
%{rlibdir}/UsingR/data
%{rlibdir}/UsingR/errata
%{rlibdir}/UsingR/Meta
%{rlibdir}/UsingR/help
%{rlibdir}/UsingR/answers
%{rlibdir}/UsingR/tsEx
%{rlibdir}/UsingR/INDEX
%{rlibdir}/UsingR/R
RPM build errors:
%{rlibdir}/UsingR/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.17-1
- initial package for Fedora