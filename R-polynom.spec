%global packname  polynom
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.6
Release:          1%{?dist}
Summary:          A collection of functions to implement a class for univariate polynomial manipulations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions to implement a class for univariate polynomial

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
%doc %{rlibdir}/polynom/CITATION
%doc %{rlibdir}/polynom/DESCRIPTION
%doc %{rlibdir}/polynom/html
%{rlibdir}/polynom/help
%{rlibdir}/polynom/R
%{rlibdir}/polynom/NAMESPACE
%{rlibdir}/polynom/INDEX
%{rlibdir}/polynom/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.6-1
- initial package for Fedora