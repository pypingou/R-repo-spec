%global packname  WilcoxCV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Wilcoxon-based variable selection in cross-validation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions to perform fast variable selection based
on the Wilcoxon rank sum test in the cross-validation or Monte-Carlo
cross-validation settings, for use in microarray-based binary

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
%doc %{rlibdir}/WilcoxCV/html
%doc %{rlibdir}/WilcoxCV/DESCRIPTION
%{rlibdir}/WilcoxCV/INDEX
%{rlibdir}/WilcoxCV/Meta
%{rlibdir}/WilcoxCV/R
%{rlibdir}/WilcoxCV/NAMESPACE
%{rlibdir}/WilcoxCV/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora