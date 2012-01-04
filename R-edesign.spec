%global packname  edesign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Maximum entropy sampling

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Maximum entropy sampling

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
%doc %{rlibdir}/edesign/DESCRIPTION
%doc %{rlibdir}/edesign/html
%{rlibdir}/edesign/libs
%{rlibdir}/edesign/Meta
%{rlibdir}/edesign/R
%{rlibdir}/edesign/help
%{rlibdir}/edesign/INDEX
%{rlibdir}/edesign/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora