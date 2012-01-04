%global packname  s20x
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.1.8
Release:          1%{?dist}
Summary:          Stats 20x

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Stats 20x functions.

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
%doc %{rlibdir}/s20x/DESCRIPTION
%doc %{rlibdir}/s20x/html
%{rlibdir}/s20x/NAMESPACE
%{rlibdir}/s20x/R
%{rlibdir}/s20x/data
%{rlibdir}/s20x/help
%{rlibdir}/s20x/INDEX
%{rlibdir}/s20x/Meta
%{rlibdir}/s20x/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.8-1
- initial package for Fedora