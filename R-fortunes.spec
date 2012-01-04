%global packname  fortunes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          R Fortunes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R Fortunes

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
%doc %{rlibdir}/fortunes/doc
%doc %{rlibdir}/fortunes/html
%doc %{rlibdir}/fortunes/DESCRIPTION
%{rlibdir}/fortunes/R
%{rlibdir}/fortunes/help
%{rlibdir}/fortunes/INDEX
%{rlibdir}/fortunes/fortunes
%{rlibdir}/fortunes/Meta
%{rlibdir}/fortunes/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora