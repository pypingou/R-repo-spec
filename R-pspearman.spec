%global packname  pspearman
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Spearman's rank correlation test

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Spearman's rank correlation test with precomputed exact null distribution
for n <= 22.

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
%doc %{rlibdir}/pspearman/html
%doc %{rlibdir}/pspearman/DESCRIPTION
%{rlibdir}/pspearman/libs
%{rlibdir}/pspearman/R
%{rlibdir}/pspearman/Meta
%{rlibdir}/pspearman/help
%{rlibdir}/pspearman/INDEX
%{rlibdir}/pspearman/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora