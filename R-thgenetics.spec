%global packname  thgenetics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Genetic Rare Variants Tests

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Tests for genetic rare variants.

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
%doc %{rlibdir}/thgenetics/DESCRIPTION
%doc %{rlibdir}/thgenetics/html
%{rlibdir}/thgenetics/R
%{rlibdir}/thgenetics/INDEX
%{rlibdir}/thgenetics/NAMESPACE
%{rlibdir}/thgenetics/Meta
%{rlibdir}/thgenetics/help
%{rlibdir}/thgenetics/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.2-1
- initial package for Fedora