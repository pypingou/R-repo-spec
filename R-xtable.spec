%global packname  xtable
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Export tables to LaTeX or HTML

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Coerce data to LaTeX and HTML tables

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
%doc %{rlibdir}/xtable/doc
%doc %{rlibdir}/xtable/DESCRIPTION
%doc %{rlibdir}/xtable/html
%doc %{rlibdir}/xtable/NEWS
%{rlibdir}/xtable/Meta
%{rlibdir}/xtable/help
%{rlibdir}/xtable/INDEX
%{rlibdir}/xtable/data
%{rlibdir}/xtable/R
%{rlibdir}/xtable/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora