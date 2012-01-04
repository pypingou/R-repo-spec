%global packname  corrsieve
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.5
Release:          1%{?dist}
Summary:          CorrSieve

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Statistical summary of Structure output.

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
%doc %{rlibdir}/corrsieve/DESCRIPTION
%doc %{rlibdir}/corrsieve/html
%{rlibdir}/corrsieve/INDEX
%{rlibdir}/corrsieve/NAMESPACE
%{rlibdir}/corrsieve/help
%{rlibdir}/corrsieve/R
%{rlibdir}/corrsieve/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.5-1
- initial package for Fedora