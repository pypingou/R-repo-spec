%global packname  cfa
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Analysis of configuration frequencies (CFA)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Analysis of configuration frequencies for simple and repeated measures,
more sample CFa, hierarchical CFA, bootstrap-CFA, functional CFA,
Kieser-Victor CFA and various plots, and Lindner's test

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
%doc %{rlibdir}/cfa/html
%doc %{rlibdir}/cfa/DESCRIPTION
%{rlibdir}/cfa/help
%{rlibdir}/cfa/R
%{rlibdir}/cfa/NAMESPACE
%{rlibdir}/cfa/INDEX
%{rlibdir}/cfa/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora