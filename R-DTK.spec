%global packname  DTK
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          Dunnett-Tukey-Kramer Pairwise Multiple Comparison Test Adjusted for Unequal Variances and Unequal Sample Sizes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package was created to analyze multi-level one-way experimental
designs. It is designed to handle vectorized observation and factor data
where there are unequal sample sizes and population variance homogeneity
can not be assumed. To conduct the Dunnett modified Tukey-Kramer test
(a.k.a. the T3 Procedure), create two vectors: one for your observations
and one for the factor level of each observation. The function,
\code{\link{gl.unequal}}, provides a means to more conveniently produce a
factor vector with unequal sample sizes. Next, use the
\code{\link{DTK.test}} function to conduct the test and save the output as
an object to input into the \code{\link{DTK.plot}} function, which
produces a confidence interval plot for each of the pairwise comparisons.
Lastly, the function (\code{\link{TK.test}}) conducts the original
Tukey-Kramer test.

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
%doc %{rlibdir}/DTK/DESCRIPTION
%doc %{rlibdir}/DTK/html
%{rlibdir}/DTK/R
%{rlibdir}/DTK/NAMESPACE
%{rlibdir}/DTK/help
%{rlibdir}/DTK/INDEX
%{rlibdir}/DTK/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1-1
- initial package for Fedora