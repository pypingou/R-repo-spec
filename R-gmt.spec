%global packname  gmt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.9
Release:          1%{?dist}
Summary:          Interface between GMT Map-Making Software and R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Interface between the GMT map-making software and R, enabling the user to
manipulate geographic data within R and call GMT commands to draw and
annotate maps in postscript format. The 'gmt' package is about interactive
data analysis, rapidly visualizing subsets and summaries of geographic
data, while performing statistical analysis in the R console.

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
%doc %{rlibdir}/gmt/DESCRIPTION
%doc %{rlibdir}/gmt/html
%doc %{rlibdir}/gmt/NEWS
%{rlibdir}/gmt/example
%{rlibdir}/gmt/NAMESPACE
%{rlibdir}/gmt/Meta
%{rlibdir}/gmt/help
%{rlibdir}/gmt/R
%{rlibdir}/gmt/data
%{rlibdir}/gmt/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.9-1
- initial package for Fedora