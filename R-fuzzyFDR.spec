%global packname  fuzzyFDR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Exact calculation of fuzzy decision rules for multiple testing

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Exact calculation of fuzzy decision rules for multiple testing. Choose to
control FDR (false discovery rate) using the Benjamini and Hochberg
method, or FWER (family wise error rate) using the Bonferroni method.
Kulinsakaya and Lewin (2007).

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
%doc %{rlibdir}/fuzzyFDR/html
%doc %{rlibdir}/fuzzyFDR/DESCRIPTION
%{rlibdir}/fuzzyFDR/NAMESPACE
%{rlibdir}/fuzzyFDR/data
%{rlibdir}/fuzzyFDR/INDEX
%{rlibdir}/fuzzyFDR/R
%{rlibdir}/fuzzyFDR/help
%{rlibdir}/fuzzyFDR/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora