%global packname  JADE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          JADE and ICA performance criteria

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-clue 


BuildRequires:    R-devel tex(latex) R-clue



%description
The package ports JF Cardoso's JADE algorithm as well as his function for
joint diagonalization. There are also several criteria for performance
evaluation of ICA algorithms.

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
%doc %{rlibdir}/JADE/html
%doc %{rlibdir}/JADE/DESCRIPTION
%{rlibdir}/JADE/ChangeLog
%{rlibdir}/JADE/Meta
%{rlibdir}/JADE/R
%{rlibdir}/JADE/NAMESPACE
%{rlibdir}/JADE/help
%{rlibdir}/JADE/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora