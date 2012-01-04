%global packname  plotrix
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2.8
Release:          1%{?dist}
Summary:          Various plotting functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Lots of plots, various labeling, axis and color scaling functions.

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
%doc %{rlibdir}/plotrix/NEWS
%doc %{rlibdir}/plotrix/html
%doc %{rlibdir}/plotrix/DESCRIPTION
%doc %{rlibdir}/plotrix/CITATION
%{rlibdir}/plotrix/INDEX
%{rlibdir}/plotrix/help
%{rlibdir}/plotrix/Meta
%{rlibdir}/plotrix/data
%{rlibdir}/plotrix/demo
%{rlibdir}/plotrix/R
%{rlibdir}/plotrix/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.8-1
- initial package for Fedora