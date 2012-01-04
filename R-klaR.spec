%global packname  klaR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.6
Release:          1%{?dist}
Summary:          Classification and visualization

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Miscellaneous functions for classification and visualization developed at
the Fakultaet Statistik, Technische Universitaet Dortmund

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
%doc %{rlibdir}/klaR/html
%doc %{rlibdir}/klaR/CITATION
%doc %{rlibdir}/klaR/DESCRIPTION
%{rlibdir}/klaR/NAMESPACE
%{rlibdir}/klaR/Meta
%{rlibdir}/klaR/R
%{rlibdir}/klaR/help
%{rlibdir}/klaR/INDEX
%{rlibdir}/klaR/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.6-1
- initial package for Fedora