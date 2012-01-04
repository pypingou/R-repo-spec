%global packname  multcompView
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Visualizations of Paired Comparisons

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
Convert a logical vector or a vector of p-values or a correlation,
difference, or distance matrix into a display identifying the pairs for
which the differences were not significantly different.  Designed for use
in conjunction with the output of functions like TukeyHSD, dist{stats},
simint, simtest, csimint, csimtest{multcomp}, friedmanmc,

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
%doc %{rlibdir}/multcompView/doc
%doc %{rlibdir}/multcompView/DESCRIPTION
%doc %{rlibdir}/multcompView/html
%{rlibdir}/multcompView/NAMESPACE
%{rlibdir}/multcompView/help
%{rlibdir}/multcompView/Meta
%{rlibdir}/multcompView/INDEX
%{rlibdir}/multcompView/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora